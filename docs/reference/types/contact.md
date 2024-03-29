# Contact

## `Contact.resolve_from_text`

This API allows us to resolve a `Contact` or a list of `Contact` objects from a given user input. For example, a recipient of a message or a contact to create a reminder for.

``` py
Contact.resolve_from_text(
    text: str
) : Contact | List[Contact]
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual Contact description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Contact | List[Contact]`    | `Contact` object or a list of `Contact` objects based on the `text` parameter to this function. |

**Example**

{==

Remind me tomorrow to postpone my dentist appointment

==}

``` py
contact = Contact.resolve_from_text("me")
```
