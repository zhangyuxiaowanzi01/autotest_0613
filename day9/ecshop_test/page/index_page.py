from common.base import Base, By


class IndexPage(Base):

    def font_text(self):
        return self.get_element_text((By.CLASS_NAME, 'f4_b'))

    def a_link(self):
        # 点击退出超链接
        self.click((By.LINK_TEXT, '退出'))
