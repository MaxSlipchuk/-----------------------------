import turtle
import modules.create_screen as m_c_screen
import modules.draw_table as m_d_table
import modules.cell_click_detection as m_c_click



m_d_table.draw_table(-100,100)


m_c_screen.screen.onclick(m_c_click.click_cell, btn=1, add=True)

    

turtle.done()





