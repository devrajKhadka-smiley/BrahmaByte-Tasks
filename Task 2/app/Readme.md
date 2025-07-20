A User has many Messages

A Room has many Messages

A Message belongs to one User and one Room


User
 └───┐
     │      (One-to-many)
     ▼
Message ───┐
     ▲     │
     │     │ (Many-to-one)
Room ◄─────┘
