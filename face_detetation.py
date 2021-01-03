import cv2 as cv
import downloader
import image_processing


def detector(*images):
    downloader.download_haarcascade()
    detect = cv.CascadeClassifier(downloader.haarcascade_path())
    lbfmodel = "lbfmodel.yaml"
    landmark_detector = cv.face.createFacemarkLBF()
    landmark_detector.loadModel(lbfmodel)
    face_counter = 0
    for original_image in images:
        image_proc = image_processing.process(original_image)
        faces = detect.detectMultiScale(image_proc)
        image = image_processing.image_read(original_image)
        _, landmarks = landmark_detector.fit(image, faces)
        face_counter += 1
        for landmark in landmarks:
            for x, y in landmark[0]:
                cv.circle(image, (x, y), 1, (255, 0, 0), 3)
        for face in faces:
            x, y, w, d = face
            cv.rectangle(image, (x, y), (w + x, d + y), (255, 255, 255), 2)
        cv.imwrite("test{}.jpg".format(face_counter), image)

