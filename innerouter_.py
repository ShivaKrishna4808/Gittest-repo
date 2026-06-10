class Orga:
    def __init__(self):
        self.inner = self.department()

    def showName(self):
        print("Organization Name: Tutorials Point")

    class department:
        def __init__(self):
            self.innerTeam = self.Team1()

        def displayDep(self):
            print("In department ")

        class Team1:
            def displayTeam(self):
                print("Team 1 of the department")

outer = Orga()

outer.showName()

inner = outer.inner
inner.displayDep()

innerTeam = inner.innerTeam

innerTeam.displayTeam()