# Google Workspace Resource Provider

The Google Workspace Resource Provider lets you manage [Google Workspace](https://workspace.google.com/) resources.

## Installing

You'll have to install this locally for now.

<!-- TODO: Update this when publishing is done. -->
<!-- 
This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumi/googleworkspace
```

or `yarn`:

```bash
yarn add @pulumi/googleworkspace
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_googleworkspace
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/pulumi/pulumi-googleworkspace/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.Googleworkspace
``` -->

## Configuration

The following configuration points are available for the `Googleworkspace` provider:

- `googleworkspace:access_token` A temporary [OAuth 2.0 access token] obtained from the Google Authorization server, i.e. the Authorization: Bearer token used to authenticate HTTP requests to Google Admin SDK APIs. This is an alternative to `credentials`, and ignores the `oauth_scopes` field. If both are specified, `access_token` will be used over the `credentials` field.
- `googleworkspace:credentials` (environment: `GOOGLEWORKSPACE_CREDENTIALS` OR `GOOGLEWORKSPACE_CLOUD_KEYFILE_JSON` OR `GOOGLE_CREDENTIALS`) Either the path to or the contents of a service account key file in JSON format you can manage key files using the Cloud Console). If not provided, the application default `credentials` will be used.
- `googleworkspace:customer_id` The customer id provided with your Google Workspace subscription. It is found in the admin console under Account Settings.
- `googleworkspace:impersonated_user_email` The impersonated user's email with access to the Admin APIs can access the Admin SDK Directory API. `impersonated_user_email` is required for all services except group and user management.
- `googleworkspace:oauth_scopes` (List of String) The list of the scopes required for your application (for a list of possible scopes, see Authorize requests)
- `googleworkspace:service_account` The service account used to create the provided `access_token` if authenticating using the `access_token` method and needing to impersonate a user. This service account will require the GCP role Service Account Token Creator if needing to impersonate a user.


<!-- TODO: Update this when the package is published. -->
<!-- ## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/foo/api-docs/). -->
