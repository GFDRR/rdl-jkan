---
attributions:
- entity:
    affiliation: null
    email: null
    name: Healthsites
    url: https://healthsites.io/
  id: Entity_1
  role: resource_provider
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://www.openstreetmap.org/
  id: Entity_2
  role: rights_holder
catalog: null
contact_point:
  affiliation: null
  email: ' mark@healthsites.io'
  name: Healthsites
  url: https://healthsites.io/
creator:
  affiliation: null
  email: null
  name: Healthsites
  url: https://healthsites.io/
dataset_id: rdls_exp-jrc_drmkc_healthsites
description: Global healthcare facilities
details: The Global Healthsites Mapping Project is an open-source initiative creating
  a comprehensive online map of healthcare facilities worldwide, making detailed location
  information easily accessible. The database includes diverse health facility types
  such as hospitals, clinics, health centers, pharmacies, and specialized care facilities
  across all countries and regions. Each facility entry contains geographical coordinates,
  facility type, name, and available attributes to support spatial analysis and healthcare
  planning. The platform serves multiple stakeholders including humanitarian organizations,
  health ministries, researchers, and emergency responders who require accurate health
  facility data for service delivery planning, gap analysis, emergency preparedness,
  and healthcare accessibility assessments. The project leverages community contributions
  and data partnerships to continuously expand and update the global healthcare facility
  inventory, supporting improved health outcomes through better spatial intelligence.
exposure:
- asset_type: null
  category: infrastructure
  id: exp_1
  metrics:
  - dimension: structure
    id: healthcare
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: Healthsites
    risk_data_type: null
    type: dataset
    url: https://healthsites.io/
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Healthsites
  url: https://healthsites.io/
publisher:
  affiliation: null
  email: null
  name: Healthsites
  url: https://healthsites.io/
purpose: To create a comprehensive global map of healthcare facilities with accessible
  location details to support health service planning, emergency response, and healthcare
  accessibility analysis worldwide.
referenced_by: []
resources:
- access_url: https://www.healthsites.io/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: This data was generated as an extract from the OpenStreetMap global
    open database (http://openstreetmap.org) by the Healthsites.io (http://healthsites.io)
    project.
  download_url: https://healthsites.io/api/public/facilities/shapefile/World/download
  format: null
  id: healthcare
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global healthcare facilities
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_drmkc_healthsites
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global Healthsites Mapping
version: '2025'
vulnerability: null
---
