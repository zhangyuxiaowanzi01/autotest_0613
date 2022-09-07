from common.base import Base, By


class IndexPage(Base):
    def font_text(self):
        return self.get_element_text((By.CLASS_NAME, 'f4_b'))
