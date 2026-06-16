---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-bangued-town-abra-province-cordillera-administrative-region-philippin
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-bangued-town-abra-province-cordillera-administrative-region-philippin
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-bangued-town-abra-province-cordillera-administrative-region-philippin
dataset_id: rdls_hl-phl_unosat_damageassessmentbanguedto_20220803
description: "UNOSAT code: EQ20220727PHL This map illustrates potentially damaged\
  \ buildings and damaged buildings in Bangued Town, Abra Province, Cordillera Administrative\
  \ Region, Philippines as detected by Pl\xE9iades satellite image acquired on 29\
  \ July 2022. Within the analyzed area, UNOSAT has identified 137 potentially damaged\
  \ buildings and 10 damaged buildings. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-bangued-town-abra-province-cordillera-administrative-region-philippin]"
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
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Pl\xE9iades satellite imagery acquired on\
    \ 29 July 2022 (2 days post-earthquake) and compared it with pre-event imagery\
    \ to detect notable changes in building structures. Damage was classified into\
    \ two categories: potentially damaged (137 buildings) and confirmed damaged (10\
    \ buildings) in Bangued Town. Results are preliminary and unvalidated field assessments."
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
- href: https://data.humdata.org/dataset/damage-assessment-in-bangued-town-abra-province-cordillera-administrative-region-philippin
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment identifying 137 potentially damaged
      and 10 confirmed damaged buildings from earthquake ground shaking
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
  description: Damage Assessment in Bangued Town, Abra Province, Cordillera Administrative
    Region, Philippines (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/EQ20220727PHL/EQ20220727PHL_gdb.zip
  format: Geodatabase
  id: resource_7619cabf
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20220727PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Bangued Town, Abra Province, Cordillera Administrative
    Region, Philippines (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/EQ20220727PHL/EQ20220727PHL_shp.zip
  format: null
  id: resource_9465df03
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20220727PHL_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_unosat_damageassessmentbanguedto_20220803
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-03'
temporal_resolution: null
title: Damage Assessment in Bangued Town, Abra Province, Cordillera Administrative
  Region, Philippines
version: null
vulnerability: null
---
