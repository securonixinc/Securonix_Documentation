---
bookCollapseSection: true
---

# Content Management

Content Management allows detection engineers to seamlessly deploy content (policies and parsers) in their environment. The Securonix content team has a content library where they upload new and modified content to share with customers. Customers have their own local content repository in the file system located at "$SECURONIX_HOME/content/data". Content administrators or detection engineers can efficiently download new and updated content, and deploy it in their SNYPR application. The following types of content can be deployed using Content Management:

* Parsers
* Third Party Intelligence
* Data Dictionary
* Active List
* Lookup Tables
* Workflow
* Policy
* Threat Models

![CM Menu](../../../CM_Menu.png "CM Menu")


Content Management has the following features:

* Content Update: Allows you to download and deploy content from the Securonix content library to the local repository. The Securonix content library stores new content and updates to the existing content.
* Commit Content: Allows you to version control your content by committing it to the Custom content library. The Custom content library is unique for each customer, and stores content created and modified by a customer.

The following illustration depicts the content workflow:

![CM Workflow](../../../CM_Workflow.png)

## Prerequisites
The following prerequisites are required to access Content Management:

1. The Securonix content library access details must be configured at Menu > Admin > Settings > Content Library.

2. A  user account with role as ROLE_CONTENT_ADMIN. When the ROLE_CONTENT_ADMIN is not assigned to the user, the Content Management option is not available.

![CM Admin](../../../CM_Prereq.png)

3. A user account with role as ROLE_COMMIT_CONTENT to commit content from Content Management.

