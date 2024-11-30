def predict_user(recognizer, users, img, y, h, x, w ):
    id, confidence = recognizer.predict(img[y:y + h, x:x + w])
    id -= 2

    # Check if confidence is less them 100 ==> "0" is perfect match
    if (confidence < 100):
        id = users[id]
        confidence = "  {0}%".format(round(100 - confidence))
    else:
        id = "inconu"
        confidence = "  {0}%".format(round(100 - confidence))
    return id, confidence