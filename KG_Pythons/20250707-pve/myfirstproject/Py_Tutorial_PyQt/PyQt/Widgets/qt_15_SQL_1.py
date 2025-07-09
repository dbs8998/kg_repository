# PyQt + SQLite3 : 키입력 데이터 저장 및 출력
# 미션: 서울시 지하철역에 설치된 공기청정기의 운전상태와 필터상태를 입출력하는 UI를 만드시오.

import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS airpurifier(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                purifierID TEXT NOT NULL,
                status INTEGER NOT NULL,
                loc TEXT NOT NULL,
                model TEXT,
                filterAge INTEGER NOT NULL,
                refilter_1 TEXT NOT NULL,
                refilter_2 TEXT NOT NULL,
                refilter_3 TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                note TEXT,
                last_filter_change TEXT NOT NULL DEFAULT '2024-01-01'
                )
            ''')
        # airpurifier가 존재해서 업데이트가 안 되는 경우
        cur.execute("PRAGMA table_info(airpurifier)")
        columns = cur.fetchall()
        column_names = [col[1] for col in columns]
        
        if 'last_filter_change' not in column_names:
            cur.execute("ALTER TABLE airpurifier ADD COLUMN  last_filter_change TEXT DEFAULT '2024-01-01'")
        
        self.conn.commit()
    
    def add_data(self, purifierID, status, loc, model, filterAge, refilter_1, refilter_2, refilter_3, date_, time_, note):
        cur = self.conn.cursor()
        cur.execute('''
            INSERT INTO airpurifier (purifierID, status, loc, model, filterAge, refilter_1, refilter_2, refilter_3, date, time, note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (purifierID, status, loc, model, filterAge, refilter_1, refilter_2, refilter_3, date_, time_, note))
        self.conn.commit()
    
    def get_all_data(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM airpurifier")
        return cur.fetchall()
    
    def get_last_filter_change(self, purifierID):
        cur = self.conn.cursor()
        cur.execute("SELECT MAX(last_filter_change) FROM airpurifier")
        result = cur.fetchone()[0]
        return QDate.fromString(result, "yyyy-MM-dd") if result else QDate(2024, 1, 1)
    
    def update_last_filter_change(self, purifierID, date):
        cur = self.conn.cursor()
        cur.execute('''
            UPDATE airpurifier
            SET last_filter_change = ?
            WHERE purifierID = ?            
        ''', (date.toString('yyyy-MM-dd'), purifierID))
        self.conn.commit()
    
    def close(self):
        self.conn.close()
        
class InputForm(QDialog):
    def __init__(self):
        super().__init__()        
        self.db = DatabaseManager('PyQt/Widgets/db/airpurifier.db')
        self.init_ui()
        
    def init_ui(self):
        # 1. 레이아웃 생성
        # main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        self.purifierID_layout = QHBoxLayout()
        self.status_layout = QHBoxLayout()
        self.datetime_layout = QHBoxLayout()
        self.filterCheck_layout = QHBoxLayout()
        self.confirm_layout = QHBoxLayout()
        
        # 2. 위젯 생성
        # entries = [loc_, purifierNum_, stat_1, stat_2, filterAge_, model_, date_,time_,note_, refilter_1, refilter_2, refilter_3, enter_, show_]
        # (purifierID = loc + purifierNum)
        # checkbox: 교체 등록
        # button: 입력, 보기
        # 2.1 loc 위젯
        locations = ['강남', '논현', '성수', '역삼', '연신내', '잠실', '종로']
        self.combo_loc = QComboBox()
        self.combo_loc.addItems(locations)    
        
        # 2.2 purifierNum 위젯
        self.spinB_purifierNum = QSpinBox()
        self.spinB_purifierNum.setRange(1, 11)
        self.spinB_purifierNum.setValue(1)
        
        # 2.3 Status 위젯
        self.radioB_purifierNum1 = QRadioButton("정상 가동")
        self.radioB_purifierNum2 = QRadioButton("가동 중지")
        
        # 2.4 filterage 위젯
        # "잔여수명 = 기대수명 - DB에서 불러온 days 계산값"
        self.label_filterage = QLabel()
        
        # 2.5 model 위젯
        models = ['A10', 'A20', 'A30', 'B11', 'B12']
        self.combo_model = QComboBox()
        self.combo_model.addItems(models)
        
        # 2.6 날짜 위젯
        self.date_widget = QDateEdit()
        self.time_widget = QTimeEdit()
        
        # 2.7 메모 위젯
        self.input_note = QLineEdit()
        
        # 2.8 필터 교체 등록
        self.checkB_refilter_1 = QCheckBox("필터1 교체")
        self.checkB_refilter_2 = QCheckBox("필터2 교체")
        self.checkB_refilter_3 = QCheckBox("필터3 교체")
        
        # 2.9 버튼 위젯
        self.button_enter = QPushButton("입력")
        self.button_call = QPushButton("보기")
        
        self.button_enter.clicked.connect(self.submit_data)
        self.button_call.clicked.connect(self.display_data)

        # 3. 레이아웃에 위젯 추가
        # 3.1/2 loc, purifierNum = purifierID
        self.purifierID_layout.addWidget(self.combo_loc)
        self.purifierID_layout.addWidget(self.spinB_purifierNum)
        form_layout.addRow("기기번호*: ", self.purifierID_layout)
        
        # 3.3 status
        self.status_layout.addWidget(self.radioB_purifierNum1)
        self.status_layout.addWidget(self.radioB_purifierNum2)
        form_layout.addRow("운전상태*: ", self.status_layout)

        # 3.4 filter age
        form_layout.addRow("필터잔여수명: ", self.label_filterage)

        # 3.5 model
        form_layout.addRow("모델명: ", self.combo_model)
        
        # 3.6 Datetime
        self.datetime_layout.addWidget(self.date_widget)
        self.datetime_layout.addWidget(self.time_widget)
        form_layout.addRow("점검일시*: ", self.datetime_layout)

        # 3.7 메모
        form_layout.addRow("점검자 메모: ", self.input_note)

        # 3.8 필터 교체 등록 여부
        self.filterCheck_layout.addWidget(self.checkB_refilter_1)
        self.filterCheck_layout.addWidget(self.checkB_refilter_2)
        self.filterCheck_layout.addWidget(self.checkB_refilter_3)
        form_layout.addRow("필터교체? ", self.filterCheck_layout)
        
        # 3.9 입력 또는 보기 버튼
        self.confirm_layout.addWidget(self.button_enter)
        self.confirm_layout.addWidget(self.button_call)
        form_layout.addRow("", self.confirm_layout)
        
        # 4. 메인 구현
        self.setLayout(form_layout)
        self.setWindowTitle("공기청정기 관리")
        self.resize(500, 400)
        self.show()
    
    def update_filter_age(self):
        purifierID_ = self.combo_loc.currentText() + str(self.spinB_purifierNum.value())
        last_change_date = self.db.get_last_filter_change(purifierID_)
        days_since_last_change = last_change_date.daysTo(QDate.currentDate())
        remaining_life = max(0, 100 - days_since_last_change) # 최소 0일
        self.label_filterage.setText(str(remaining_life))
    
    def validate_inputs(self, purifierID, status, loc, model, filterAge, date_, time_, note):
        if not purifierID or not status or not loc or not date_ or not time_:
            QMessageBox.warning(self, "입력오류", "모든 필수항목을 입력해주세요.")
            return False
        return True
    
    def submit_data(self):
        # if not self.validate_inputs():
        #     return
        
        loc_ = self.combo_loc.currentText()
        purifierNum_ = self.spinB_purifierNum.value()
        purifierID_ = loc_ + str(purifierNum_)
        status_ = 1 if self.radioB_purifierNum1.isChecked() else 0
        filterAge_ = 30  # 추후 계산값으로 대체할것!
        model_ = self.combo_model.currentText()
        date_ = self.date_widget.text()
        time_ = self.time_widget.text()
        note_ = self.input_note.text()
        refilter_1 = "Yes" if self.checkB_refilter_1.isChecked() else "No"
        refilter_2 = "Yes" if self.checkB_refilter_2.isChecked() else "No"
        refilter_3 = "Yes" if self.checkB_refilter_3.isChecked() else "No"
        
        if not self.validate_inputs(purifierID_, status_, loc_, model_, filterAge_, date_, time_, note_):
            return

        self.db.add_data(purifierID_, status_, loc_, model_, filterAge_, refilter_1, refilter_2, refilter_3, date_, time_, note_)
        if refilter_1=="Yes" or refilter_2=="Yes" or refilter_3=="Yes":
            self.db.update_last_filter_change(purifierID_, self.date_widget.date())
        QMessageBox.information(self, "관리내역", "저장 완료")
        self.update_filter_age()

    def display_data(self):
        data = self.db.get_all_data()
        display_text = "\n".join([f"ID: {row[0]}, 청정기번호: {row[1]}, 상태: {row[2]}, 위치: {row[3]}, 모델: {row[4]}, 필터잔여수명: {row[5]}, 1번필터교체: {row[6]}, 2번필터교체: {row[7]}, 3번필터교체: {row[8]}, 날짜: {row[9]}, 시간: {row[10]}, 메모: {row[11]}" for row in data])
        QMessageBox.information(self, "저장된 데이터", display_text)

    def closeEvent(self, event):
        self.db.close()
        event.accept()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    main = InputForm()
    sys.exit(app.exec_())
