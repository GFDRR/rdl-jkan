---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu
dataset_id: rdls_el-vut_unosat_buildingsdamageassessment_20200416
description: 'UNOSAT code: TC20200403VUT This map illustrates potentially damaged
  structures and buildings in south of Sanma Province, Vanuatu as detected by satellite
  image acquired after landfall of the Tropical Cyclone Harold-20 on 6 April 2020.
  UNITAR-UNOSAT analysis identified about 5,200 potentially damaged structures in
  the analysis extent across the south of Sanma province within the cloud free areas.
  Taking into account the pre-building footprints provided by Humanitarian OpenStreetMap,
  this represents about 33% of the total number of structures/buildings within the
  analyzed cloud free areas. Please note that some areas could not be analyzed due
  to the cloud cover. Total and final estimates by municipality are summarized in
  the table below. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building footprints and structures in south Sanma Province identified
      from satellite imagery and OpenStreetMap
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
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-Tropical Cyclone Harold satellite imagery acquired on
    6 April 2020 to detect structural damage through visual change detection. Approximately
    5,200 damaged structures were identified in cloud-free areas of south Sanma Province,
    representing 33% of the total building inventory.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-in-south-of-sanma-province-vanuatu
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Harold assessed via
      post-event satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Buildings Damage Assessment & Related Density in South of Sanma Province,
    Vanuatu (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VU/TC20200403VUT/TC20200403VUT_gdb.zip
  format: Geodatabase
  id: resource_77f5d373
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200403VUT_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Buildings Damage Assessment & Related Density in South of Sanma Province,
    Vanuatu (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VU/TC20200403VUT/TC20200403VUT_SHP.zip
  format: null
  id: resource_fe99c9c8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200403VUT_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-vut_unosat_buildingsdamageassessment_20200416
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-16'
temporal_resolution: null
title: Buildings Damage Assessment & Related Density in South of Sanma Province, Vanuatu
version: null
vulnerability: null
---
