---
attributions:
- entity:
    affiliation: null
    email: null
    name: GLOBHE (Crowddroning)
    url: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-thyolo-malawi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-thyolo-malawi
creator:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-thyolo-malawi
dataset_id: rdls_he-mwi_globhe_posttropicalstormchalanem_20210110
description: 'Drone orthomosaic. Post Tropical Storm Chalane Mapping, Malawi conducted
  with Crowddroning by GLOBHE. More maps and data available on demand upon request
  from locations globally at: https://globhe.com/ MORE CROWDDRONING BY GLOBHE Web:
  https://globhe.com/ Facebook: https://www.facebook.com/Crowddroning Twitter: https://twitter.com/globhedrones
  Instagram: https://www.instagram.com/globhedrones/ LinkedIn: https://www.linkedin.com/company/globhedrones/.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-thyolo-malawi]'
details: null
exposure:
- asset_type:
    description: Building structures and infrastructure visible in drone orthomosaic
      imagery
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Vegetation and land cover features affected by storm impacts
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Drone orthomosaic imagery was acquired post-event over Thyolo district,
    Malawi following Tropical Storm Chalane. The aerial imagery was processed by GLOBHE
    using crowddroning methodology to create georeferenced orthomosaics documenting
    physical storm impacts on buildings and landscape features.
  sources:
  - id: source_1
    license: null
    name: GLOBHE (Crowddroning)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-thyolo-malawi
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Drone orthomosaic. Post Tropical Storm Chalane Mapping, Malawi conducted
    with Crowddroning by GLOBHE. More maps and data available on demand upon request
    from locations globally at https://globhe.com/
  download_url: https://www.dropbox.com/s/j39vtioeywmkhxw/Post%20Tropical%20Storm%20Chalane%20Mapping%2C%20Thyolo%2C%20Malawi.tif?dl=1
  format: null
  id: resource_52a9dd3b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Orthomosaic map (TIFF)
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mwi_globhe_posttropicalstormchalanem_20210110
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-01-10'
temporal_resolution: null
title: Post Tropical Storm Chalane Mapping, Thyolo, Malawi
version: null
vulnerability: null
---
