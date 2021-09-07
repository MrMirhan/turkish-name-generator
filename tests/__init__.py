import trnamegen as trn

# Random woman name with surname
rwn = trn.randomName(2)

# Random man name with surname
rmn = trn.randomName(1)

# Random name with surname
rn = trn.randomName(1)

# Random woman first name
rwfn = trn.firstName(2)

# Random man first name
rmfn = trn.firstName(1)

# Random first name
rfn = trn.firstName(0)

# Random last name
rln = trn.lastName()

print(rwn, rmn, rn, rwfn, rmfn, rfn, rln)