# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "google/gce"
  
  config.vm.provider :google do |google, override|
    google.google_project_id = "proyectoiv-2"
    google.google_client_email = "adrian@proyectoiv-2.iam.gserviceaccount.com "
    google.google_json_key_location = "~/.ssh/proyectoiv-2-d237bacf85b8.json"

    # Define the name of the instance.
    google.name = "workwaitqueue"

    # Set the zone where the instance will be located. To find out available zones:
    # `gcloud compute zones list`.
    google.zone = "europe-west4-a"

    # Set the machine type to use. To find out available types:
    # `gcloud compute machine-types list --zone asia-east1-c`.
    google.machine_type = "n1-standard-2"

    # Set the machine image to use. To find out available images:
    # `$ gcloud compute images list`.
    google.image = "ubuntu-1604-xenial-v20190112"

    override.ssh.username = "archdri"
    override.ssh.private_key_path = "/home/archdri/.ssh/id_rsa"    
  end

  # Provisionamiento - Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "ansible.yml"
  end
end
