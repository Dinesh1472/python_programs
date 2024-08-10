try:
    temp="""In the heart of the bustling city, where the streets hummed with a symphony of car
    horns pedestrian chatter, stood a quaint little café. Its weathered brick facade exuded a
    timeless charm,the aroma of freshly ground coffee beans wafted out, enticing passersby to step inside. Th
    e interior was a sanctuary of warmth tranquility, soft jazz melodies floating hidden speakers sunlight
    streaming through large, vintage windows adorned lace curtains. Patrons huddled over steaming mugs, their conversations
    blending into a soothing buzz that filled the air. It was here, amidst the comforting embrace of good coffee gentle ambiance,
    that stories unfolded moments lingered just a little longer."""


    print(temp.count('models.py'))
    print('--'*40)

    print(temp.index('i'))
    print('--'*40)

    print(temp.find('dinesh'))
    print('--'*40)
    if 'error' in temp:
        print('errormis present there')
    else:
        print('error is not present')

except exception as e:
    print(e)
