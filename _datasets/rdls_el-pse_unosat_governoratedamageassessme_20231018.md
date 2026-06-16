---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-gaza-strip-occupied-palestinian-territory
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-gaza-strip-occupied-palestinian-territory
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-gaza-strip-occupied-palestinian-territory
dataset_id: rdls_el-pse_unosat_governoratedamageassessme_20231018
description: 'UNOSAT code CE20231007PSE This map illustrates a satellite-detected
  damage and destruction to buildings within the area of interest in the Gaza Governorate,
  Gaza Strip, based on an image collected on 10 October 2023 (partially clouded) when
  compared to an image collected on 10 May 2023. According to satellite imagery analysis,
  UNOSAT identified 228 destroyed structure, 148 severely damaged structures and 365
  moderately damaged structures, for a total of 741 buildings. The two most affected
  areas appear to be between Southern Remal and As Sabra neighborhoods (inset 1),
  and on the western outskirt of the Old City, north of At Turukman neighborhood.
  Among the affected structures, UNOSAT identified one school compound, namely the
  Omar Bin Abd Alaz school, visibly destroyed (see inset 2). This is a preliminary
  analysis and has not yet been validated in the field.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-gaza-strip-occupied-palestinian-territory]'
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
    description: Building stock in Gaza Governorate classified by damage severity
      from satellite imagery
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
  description: UNOSAT analysts compared satellite imagery from 10 May 2023 (baseline)
    and 10 October 2023 (post-event) to detect changes in building conditions across
    Gaza Governorate. Damage classification was performed through visual interpretation
    of satellite imagery, categorizing structures into destroyed, severely damaged,
    and moderately damaged classes. The resulting geodatabase contains spatial polygons
    and damage counts for the affected area.
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
- href: https://data.humdata.org/dataset/unosat-gaza-governorate-damage-assessment-gaza-strip-occupied-palestinian-territory
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      detected via satellite imagery comparison
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
  description: Palestine - UNOSAT Gaza Governorate Damage Assessment - Gaza Strip,
    Occupied Palestinian Territory (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3690/UNOSAT_CE20231007PSE_Gaza_Governorate_DA_20231010_GDB.zip
  format: Geodatabase
  id: resource_f853011a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20231007PSE_Gaza_Governorate_DA_20231010_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_governoratedamageassessme_20231018
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
  start: '2023-10-18'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Governorate Damage Assessment - Gaza Strip, Occupied
  Palestinian Territory
version: null
vulnerability: null
---
