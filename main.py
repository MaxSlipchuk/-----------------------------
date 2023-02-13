import turtle
import modules.create_screen as c_screen
import modules.draw_table as d_table
import modules.cell_click_detection as c_click


d_table.draw_table(-100,100)

c_screen.screen.onclick(c_click.click_cell, btn=1, add=True)

turtle.done()





