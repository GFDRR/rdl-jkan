---
attributions:
- entity:
    affiliation: null
    email: null
    name: Faculty of Geography, Autonomous University of the State of Mexico (UAEMex)
    url: https://data.humdata.org/dataset/damage-assessment-in-xochimilco-and-tlahuac-municipalities-federal-state-mexico-2712
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-xochimilco-and-tlahuac-municipalities-federal-state-mexico-2712
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-xochimilco-and-tlahuac-municipalities-federal-state-mexico-2712
dataset_id: rdls_lss-mex_unosat_damageassessmentxochimilc_20171102
description: 'This map illustrates satellite-detected, potentially damaged structures
  in some affected colonies located in Xochimilco and Tlahuac Municipalities, Federal
  District, Mexico. The analysis was performed by Faculty of Geography of the Autonomous
  University of the State of Mexico (UAEMex) using as post-event WorldView-2 satellite
  imagery acquired 20 September 2017. UAEMex identified 87 potentially damaged structures
  from which 63 are located in Santa Maria Nativitas colony and surroundings. Please
  do not hesitate to send feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-xochimilco-and-tlahuac-municipalities-federal-state-mexico-2712]'
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
  description: Post-event damage assessment conducted by UAEMex using WorldView-2
    satellite imagery acquired on 20 September 2017, comparing pre- and post-earthquake
    imagery to identify structural damage. UNOSAT analysts reviewed satellite imagery
    and determined notable changes between images to map 87 potentially damaged structures
    in Xochimilco and Tlahuac municipalities, with 63 located in Santa Maria Nativitas
    colony and surroundings.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Faculty of Geography, Autonomous University of the State of Mexico (UAEMex)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-xochimilco-and-tlahuac-municipalities-federal-state-mexico-2712
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake detected via satellite imagery
      analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Damage Assessment in Xochimilco and Tlahuac Municipalities, Federal
    State, Mexico (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_068a8129
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Xochimilco and Tlahuac Municipalities, Federal
    State, Mexico (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_15600fcf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mex_unosat_damageassessmentxochimilc_20171102
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-02'
temporal_resolution: null
title: Damage Assessment in Xochimilco and Tlahuac Municipalities, Federal State,
  Mexico
version: null
vulnerability: null
---
