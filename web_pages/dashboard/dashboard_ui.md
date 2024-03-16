<|{occu}|selector|lov={occupation}|on_change=on_change_Occu|dropdown|class_name=m1|>

<br/>

<|card|
**Total Orders**{:.color-primary}
<|{Orders}|text|class_name=h2|>
|>
<br/>


<|layout|columns=1 1|gap=100px|class_name=m2|
<|{overlay_data}|chart|mode=none|x=Occupation|y={y_labels}|options={options}|>
<|{pie_data}|chart|type=pie|values=values|labels=labels|>

|>

<br/>
<|{bar_data}|chart|type=bar|x=Occupation |y=Orders|layout={bar_design}|>

<br/>
<|{bubble_data}|chart|mode=markers|x=Occupation |y=States|marker={bubble_marker}|text=Texts|>
<br/>
<|{tree_data}|chart|type=treemap|labels=label|values=values|>
|>