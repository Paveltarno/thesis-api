# Event

Events can be public or private. Public events are for example a concert in the park or a game, where there is a general knowledge about the event and its details. A private event can appear as an entry in the user calendar and include information about the event in a calendar app.

## `Event.find`

This API provides us with events information.

``` py
Event.find(
    date_time: Optional[DateTime],
    location: Optional[Location],
    event_name: Optional[EventName],
    event_calendar: Optional[EventCalendar],
    resource: Optional[Resurce]
) : Iterable[EventEntity]
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `date_time`        | `DateTime`  | Yes        | Date and time of the event        |
| `location`        | `Location`  | Yes        | Event location        |
| `event_category`        | `EventCategory`  | Yes        | The event name        |
| `event_name`        | `EventName`  | Yes        | The event name        |
| `event_calendar`        | `EventCalendar`  | Yes        | The calendar name where the event should be listed |
| `resource`        | `Resource`  | Yes        | The event resource application |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Iterable[EventEntity]`    | Iterable of `EventEntity` objects |

**Example**

{==

When is the Eagles concert with Chris Stapleton coming to Dallas?

==}

``` py
event_name = EventName.resolve_from_text("Eagles concert with Chris Stapleton")
event_category = EventCategory.resolve_from_text("concert")
location = Location.resolve_from_text("Dallas")
events = Event.find(
    event_name=event_name,
    event_category=event_category,
    location=location
)
response = events
Responder.respond(response=response)
```

**Example**

{==

Show me my next meeting on my work calendar.

==}

``` py
event_category = EventCategory.resolve_from_text("meeting")
event_calendar = EventCalendar.resolve_from_text("my work calendar")
events = Event.find(
    event_category=event_category,
    event_calendar=event_calendar
)
events = events.first()
response = events
Responder.respond(response=response)
```
