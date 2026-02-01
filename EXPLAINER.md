# Playto Community Feed Backend – Explanation

This document explains the design and working of the Playto Community Feed backend built using Django and Django REST Framework.

---

## 1. Overview

The backend provides APIs for a community feed where users can create posts and comments.
Comments support replies, forming a nested (threaded) structure.
A leaderboard endpoint is also included to rank users based on activity.

---

## 2. Nested Comments Design

Each comment belongs to a post and may optionally have a parent comment.

- If `parent` is empty → it is a top-level comment
- If `parent` is set → it is a reply to another comment

This structure allows unlimited nesting of comments.

Nested comments are returned using recursive serializers so replies appear inside their parent comment in the API response.

---

## 3. Posts API

The `/api/posts/` endpoint returns:
- Post details
- Author information
- Top-level comments
- Nested replies inside comments

This makes it easy for a frontend to render a threaded discussion without extra processing.

---

## 4. Leaderboard Implementation

The leaderboard is based on user activity (karma events).

- Each activity is stored as a karma event
- Events include user, action type, and timestamp
- The leaderboard endpoint aggregates these events
- Only recent activity (last 24 hours) is considered

This approach prevents abuse and ensures fair rankings.

---

## 5. Admin Panel Usage

The Django admin panel is used for:
- Creating users
- Managing posts
- Managing comments
- Assigning parent comments for nested replies

This allows easy testing and data management without requiring a frontend.

---

## 6. Data Validation and Safety

- Backend validations prevent invalid data
- Relationships ensure comments always belong to a post
- Clean separation of models, serializers, and views improves maintainability

---

## 7. Technology Choice

Django REST Framework was chosen because:
- It enables fast API development
- Serialization is simple and powerful
- It integrates well with frontend frameworks
- It is secure and scalable

---

## 8. Conclusion

This backend fulfills all the requirements of the Playto internship task by providing:
- A working REST API
- Nested comment support
- Leaderboard logic
- Admin-managed data

The project is complete and ready for evaluation.
