workspace "aadarchi-documentation-system" {
	model {
		person_user = person "RSS Consumer" "A user of this software system."
		external_website = softwareSystem "An external website" "A website producing a RSS feed"
		mySystem = softwareSystem "RSS Reader" "Our global rss reading system" "python, flask" {
			feedGraber = container "Feed graber" "Container responsible for updating the feeds database" "python" {
				this -> external_website "Get website latest informations"
				person_user -> this "Run the Python script to get some news"
			}
			userBackend = container "Feed presenter backend" "Container responsible for user viewed data" {

			}
			userFrontend = container "Feed presente frontend" "Container presenting user data in the browser" "htmx" "browser" {
				person_user -> this "Uses UI"
				this -> userBackend "Process requests"
			}
			database = container "Database" "data storage for all infos" "" "database" {
				feedGraber -> this "Read feeds URLs"
				feedGraber -> this "Writes feeds items"
				userBackend -> this "Writes user subscriptions"
				userBackend -> this "Read feeds items"
				userBackend -> this "Mark feed item read for one user"
			}
		}
		phase1 = deploymentEnvironment "Phase 1" {
			deploymentNode "Developer machine" "As a start, we use the dev machine" "" "" "1" {
				containerInstance feedGraber
			}
		}
		phase2 = deploymentEnvironment "Phase 2" {
			deploymentNode "Developer machine" "As a start, we use the dev machine" "" "" "1" {
				deploymentNode "Python runtime" "All python code run in the same runtime" {
					containerInstance feedGraber
					containerInstance userBackend
				}
				deploymentNode "Database server" {
					containerInstance database
				}
			}
		}
		phase3 = deploymentEnvironment "Phase 3" {
			deploymentNode "Developer machine" "As a start, we use the dev machine" "" "" "1" {
				containerInstance userFrontend
				containerInstance userBackend
			}
			deploymentNode "Central feed graber" "A feed graber server" "Docker" {
				containerInstance feedGraber
			}
			deploymentNode "Database host" {
				containerInstance database
			}
		}
		phase4 = deploymentEnvironment "Phase 4" {
			deploymentNode "Docker compose" {
				containerInstance userFrontend
				containerInstance userBackend
				containerInstance feedGraber
			}
			deploymentNode "Database server" {
				containerInstance database
			}
		}
	}
	views {
		systemContext "mySystem" "SystemContext" "Illustration of mySystem usage" {
			include *
			autoLayout
		}
		container "mySystem" "system_containers" "mySystem containers" {
			include *
			autoLayout
		}
		deployment * phase1 phase1_deployment {
			include *
			autoLayout
		}
		deployment * phase2 phase2_deployment {
			include *
			autoLayout
		}
		deployment * phase3 phase3_deployment {
			include *
			autoLayout
		}
		deployment * phase4 phase4_deployment {
			include *
			autoLayout
		}

        theme default
        styles {
            element "mobile" {
                shape MobileDevicePortrait
            }
			element "browser" {
				shape WebBrowser
			}
            element "robot" {
                shape Robot
            }
            element "database" {
                shape Cylinder
            }
            element "messaging" {
                shape "pipe"
            }
        }
	}

}