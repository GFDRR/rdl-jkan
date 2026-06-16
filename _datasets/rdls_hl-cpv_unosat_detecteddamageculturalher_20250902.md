---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-to-cultural-heritage-in-the-area-of-cova-ribeira-paul-and-torre-natural-park-santo-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-to-cultural-heritage-in-the-area-of-cova-ribeira-paul-and-torre-natural-park-santo-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-to-cultural-heritage-in-the-area-of-cova-ribeira-paul-and-torre-natural-park-santo-
dataset_id: rdls_hl-cpv_unosat_detecteddamageculturalher_20250902
description: 'UNOSAT code: FL20250812CPV This map shows possible damage to cultural
  heritage was detected 1.3 km west of the park based on a very high resolution satellite
  image collected 16 August 2025 when compared to very high resolution satellite imagery
  from 9 February 2025. Specifically, possible damage was detected to a section of
  traditional, terraced agricultural fields (inset 1). This traditional form of agriculture
  is named under Criterion (v) as one of the justifications for the area''s Outstanding
  Universal Value and its inclusion on the UNESCO Tentative List. Additionally, water
  and mud flows were detected both within and around the park. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-to-cultural-heritage-in-the-area-of-cova-ribeira-paul-and-torre-natural-park-santo-]'
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
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared very high resolution satellite imagery from\
    \ 16 August 2025 (post-event) with baseline imagery from 9 February 2025 to detect\
    \ damage to terraced agricultural fields in the Cova, Ribeira Pa\xFAl and Torre\
    \ Natural Park area. Damage polygons were digitized and attributed with area measurements\
    \ and sensor metadata to produce a post-event damage assessment dataset."
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
- href: https://data.humdata.org/dataset/damage-to-cultural-heritage-in-the-area-of-cova-ribeira-paul-and-torre-natural-park-santo-
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct damage to traditional terraced agricultural fields detected
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: "Satellite-detected damage to cultural heritage in the area of Cova,\
    \ Ribeira Pa\xFAl and Torre Natural Park, Santo Ant\xE3o, Cabo Verde, as of 16\
    \ August 2025 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4190/FL20250812CPV_gdb.zip
  format: Geodatabase
  id: resource_9666c4c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Satellite-detected damage to cultural heritage in the area of Cova,\
    \ Ribeira Pa\xFAl and Torre Natural Park, Santo Ant\xE3o, Cabo Verde, as of 16\
    \ August 2025 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4190/FL20250812CPV_SHP.zip
  format: null
  id: resource_1d617934
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250812CPV_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cpv_unosat_detecteddamageculturalher_20250902
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-09-02'
temporal_resolution: null
title: "Satellite-detected damage to cultural heritage in the area of Cova, Ribeira\
  \ Pa\xFAl and Torre Natural Park, Santo Ant\xE3o, Cabo Verde, as of 16 August 2025"
version: null
vulnerability: null
---
