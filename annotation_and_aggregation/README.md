# Annotation and Aggregation Challenge
It is common to need to compute values on each object in a queryset. One way to do this is through a serializer method, as shown in the `UserSerializer`.
However, this pattern can cause queries to be spurred unnecessarily, and much of this computation can occur within the database.
Use annotations and aggregation by overriding `UserViewSet.get_queryset`. Make `test_users_endpoint_has_reasonable_query_count` pass.

In order to participate in this challenge, create a PR with your GitHub username as the name. There will be a comment on your PR when it gets
approved.

# skeletor [<img src="https://ckcollab.com/assets/images/badges/badge.svg" alt="CKC" height="20">](https://ckcollab.com)
&nbsp;<br>
<img src="docs/skeletor_full.png" alt="CKC" width="420" align="left">
