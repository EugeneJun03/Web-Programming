import os

class m_db:
    def __init__(self):
        self.m_db_list=[]
        self.row_count=1

    class content_guide:
        def __init__(self):
            self.num=None
            self.title=None
            self.subjects=[]
            self.time=None
        
        def __str__(self):
            return f"{self.title} / {type(self.subjects)} / {self.time}"

    def mdb_read(self, row=None):
        if row==None:
            total_list=[]
            for idx in range(len(self.m_db_list)):
                temp_row={'num':self.m_db_list[idx].num, 'title':self.m_db_list[idx].title, 'time':self.m_db_list[idx].time}
                total_list.append(temp_row)
            return total_list
        
        for idx in range(len(self.m_db_list)):
            if self.m_db_list[idx].num==row:
                num=self.m_db_list[idx].num
                title=self.m_db_list[idx].title
                subjects=self.m_db_list[idx].subjects.split(",")
                time=self.m_db_list[idx].time
                return {'num':num, 'title':title, 'subjects':subjects, 'time':time}

    def mdb_write(self, content):
        content.num=self.row_count
        self.row_count=self.row_count+1
        self.m_db_list.append(content)

    def mdb_modify(self, content_num, content):
        for idx in range(len(self.m_db_list)):
            if self.m_db_list[idx].num==content_num:
                content.num=self.m_db_list[idx].num
                self.m_db_list[idx]=content

    def mdb_delete(self, content_num):
        for idx in range(len(self.m_db_list)):
            if self.m_db_list[idx].num==content_num:
                del self.m_db_list[idx]
                break;

    def get_content_guide_obj(self):
        instance=self.content_guide()
        return instance

m_db_connection=m_db()

# data sample
sample_content1=m_db_connection.get_content_guide_obj()
sample_content1.title="첫 번째 테스트 샘플입니다"
sample_content1.subjects="물리,생물"
sample_content1.time="2023-05-15T04:28:33.663Z"
m_db_connection.mdb_write(sample_content1)

sample_content2=m_db_connection.get_content_guide_obj()
sample_content2.title="두 번째 테스트 샘플입니다"
sample_content2.subjects="화학,지구"
sample_content2.time="2023-05-16T04:28:33.663Z"
m_db_connection.mdb_write(sample_content2)