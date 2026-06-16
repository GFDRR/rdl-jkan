---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update
dataset_id: rdls_el-pse_unosat_governoratedamageassessme_20231020
description: 'UNOSAT code CE20231007PS UNOSAT''s satellite-detected damage and destruction
  to buildings within the area of interest in the Gaza Governorate, Gaza Strip, based
  on an image collected on 15 October 2023 compared to an image collected on 10 October
  2023 (partially clouded), and 10 May 2023 shows a total of 533 destroyed structures,
  640 severely damaged structures, and 1273 moderately damaged structures, for a total
  of 2246 affected buildings as of 15 October 2023. The most affected area appears
  to be the one south of Ash Shuja''iyeh neighborhood (inset 1), with clouds covered
  on the 10 October 2023 image. Among the new affected structures, UNOSAT identified
  two school compounds, namely the Elnoor W Alaml School, moderately affected, and
  the Islamic University of Gaza, previously cloud-covered and now severely damaged.
  Additionally, UNOSAT identified 45 affected road sections, either by impact craters
  or by debris. This is a preliminary analysis and has not yet been validated in the
  field.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update]'
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
    description: Building stock classified by damage severity (destroyed, severely
      damaged, moderately damaged)
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
  description: UNOSAT analysts compared satellite imagery from 15 October 2023 against
    baseline images from 10 May 2023 and 10 October 2023 to detect structural damage
    through visual interpretation of notable changes in building footprints and conditions.
    Damage classifications (destroyed, severely damaged, moderately damaged) were
    assigned to individual structures and aggregated to produce impact statistics
    for the Gaza Governorate.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-update
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction assessed
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Palestine - UNOSAT Gaza Governorate Damage Assessment Update (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3698/CE20231007PSE_Gaza_20231015_GDB.zip
  format: Geodatabase
  id: resource_2077f7f8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20231007PSE_Gaza_20231015_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - UNOSAT Gaza Governorate Damage Assessment Update (KML file)
  download_url: https://unosat.org/static/unosat_filesystem/3698/CE20231007PSE_North_Gaza_Governorate_DA_20231015.kmz
  format: null
  id: resource_6fa137dc
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20231007PSE_North_Gaza_Governorate_DA_20231015.kmz
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_governoratedamageassessme_20231020
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-20'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Governorate Damage Assessment Update
version: null
vulnerability: null
---
