---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-in-providencia-island-providencia-and-santa-catalina-department-colombia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldView-2 satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-in-providencia-island-providencia-and-santa-catalina-department-colombia
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-providencia-island-providencia-and-santa-catalina-department-colombia
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-providencia-island-providencia-and-santa-catalina-department-colombia
dataset_id: rdls_lss-col_unosat_damageassessmentprovidenc_20201124
description: 'UNOSAT code: TC20201123COL This map illustrates potentially damaged
  structures and buildings in Providencia Island, Providencia and Santa Catalina Department
  of Colombia as detected by satellite image acquired after landfall of the Tropical
  Cyclone IOTA on 17 November 2020. UNITAR-UNOSAT analysis used a WorldView-2 image
  acquired on 21 November 2020 as a post-event image. Within the Island boundary,
  UNITAR-UNOSAT identified in the cloud-free zones 1,110 damaged structures. Taking
  into account the pre-building footprints provided by Humanitarian OpenStreetMap,
  this represents about 90% of the total number of structures within the analyzed
  cloud-free areas.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-providencia-island-providencia-and-santa-catalina-department-colombia]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-event WorldView-2 satellite imagery acquired 4 days after
    Tropical Cyclone IOTA landfall on 17 November 2020 to identify and count damaged
    structures in cloud-free zones of Providencia Island. The resulting damage assessment
    dataset contains 1,110 identified damaged structures with spatial geometry.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WorldView-2 satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-providencia-island-providencia-and-santa-catalina-department-colombia
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone IOTA detected via satellite
      imagery comparison
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
  description: Damage Assessment in Providencia Island, Providencia and Santa Catalina
    Department, Colombia as of 21 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/CO/TC20201123COL/TC20201123COL_gdb.zip
  format: Geodatabase
  id: resource_8434511a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201123COL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Providencia Island, Providencia and Santa Catalina
    Department, Colombia as of 21 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/CO/TC20201123COL/TC20201123COL_SHP.zip
  format: null
  id: resource_03d1adb8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201123COL_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_unosat_damageassessmentprovidenc_20201124
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-24'
temporal_resolution: null
title: Damage Assessment in Providencia Island, Providencia and Santa Catalina Department,
  Colombia as of 21 November 2020
version: null
vulnerability: null
---
