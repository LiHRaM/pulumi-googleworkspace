package shim

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/hashicorp/terraform-provider-googleworkspace/internal/provider"
)

func Provider() *schema.Provider {
	return googleworkspace.New("v0.7.0")()
}
