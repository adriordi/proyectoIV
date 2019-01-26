# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "google/gce"

  config.vm.provider :google do |google, override|
    google.google_project_id = "proyectoiv-2"
    google.google_client_email = "adrian@proyectoiv-2.iam.gserviceaccount.com "
    google.google_json_key_location = "~/.ssh/proyectoiv-2-d237bacf85b8.json"

    google.name = "workwaitqueue"
    google.zone = "europe-west4-a"
    google.machine_type = "n1-standard-2"
    google.image = "ubuntu-1604-xenial-v20190112"

    override.ssh.username = "archdri"
    override.ssh.private_key_path = "/home/archdri/.ssh/google_compute_engine"    
  end
  
  # Provisionamiento con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.verbose = "vvvv"
    ansible.playbook = "./provision/playbook.yml"
  end
end
