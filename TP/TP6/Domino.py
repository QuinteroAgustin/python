class Domino:
    face_a = 0
    face_b = 0

    def __init__(self, face_a = 0, face_b = 0):
        self.face_a = face_a
        self.face_b = face_b

    def afficher_points(self):
        print("Face A : {}, face B : {}".format(self.face_a, self.face_b))

    def valeur(self):
        return int(self.face_a+self.face_b)
    