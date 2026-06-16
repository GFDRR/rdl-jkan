---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS Earthquake Hazards Program
    url: https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025
dataset_id: rdls_hl-mmr_unosat_detecteddamageculturalher_20250417
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map shows the locations
  where damage was detected based on a very high resolution satellite image collected
  03 April 2025 when compared to very high resolution satellite imagery from 23 March
  2025. The USGS shake map indicates the intentsity of the earthquake measured 8.0
  - 8.5 in this area. Across the site 11 damaged cultural heritage locations were
  observed and an additional 3 have possible damage. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025]'
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
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared very high resolution satellite imagery acquired
    before (23 March 2025) and after (03 April 2025) the 28 March 2025 earthquake
    to detect structural damage to cultural heritage locations in Min Kun. Ground
    motion intensity data from USGS shake maps provided the hazard context. Damage
    was classified as confirmed (11 sites) or possible (3 sites) based on visual interpretation,
    with field validation pending.
  sources:
  - id: source_1
    license: null
    name: USGS Earthquake Hazards Program
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
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
- href: https://data.humdata.org/dataset/satellite-detected-damage-to-cultural-heritage-in-min-kun-as-of-03-april-2025
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Satellite-detected damage to 11 confirmed and 3 possible cultural
      heritage sites from earthquake ground shaking
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Myanmar - Satellite-detected damage to cultural heritage in Min Kun
    as of 03 April 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4109/GDB.zip
  format: Geodatabase
  id: resource_4e2ffdea
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Myanmar - Satellite-detected damage to cultural heritage in Min Kun
    as of 03 April 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4109/SHP.zip
  format: null
  id: resource_19bad087
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_unosat_detecteddamageculturalher_20250417
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-17'
temporal_resolution: null
title: Myanmar - Satellite-detected damage to cultural heritage in Min Kun as of 03
  April 2025
version: null
vulnerability: null
---
