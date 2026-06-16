---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-over-pentecost-island-penama-province-vanuatu-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-over-pentecost-island-penama-province-vanuatu-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-over-pentecost-island-penama-province-vanuatu-
dataset_id: rdls_hl-vut_unosat_buildingsdamageassessment_20231101
description: 'UNOSAT code TC20231023VUT, GDACS Id: 1001027 This map illustrates potentially
  damaged, damaged and destroyed structures density in Pentecost Island, Penama Province,
  Vanuatu as observed from a WorldView-2 imagery acquired on 29 October 2023 at 09:39
  local time. Over Penama islands, 1,704 buildings are identified as destroyed, 835
  as damaged and 1,779 as potentially damaged. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to the United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-over-pentecost-island-penama-province-vanuatu-]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed WorldView-2 satellite imagery acquired on
    29 October 2023 over Pentecost Island, Penama Province, Vanuatu, comparing multi-temporal
    images to detect structural damage from tropical cyclone Lola. Building damage
    was classified into three categories (destroyed, damaged, potentially damaged)
    through visual interpretation and change detection analysis.
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
- href: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-over-pentecost-island-penama-province-vanuatu-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from tropical cyclone Lola: 1,704 destroyed,
      835 damaged, 1,779 potentially damaged structures'
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
  description: Buildings Damage Assessment & Related Density over Pentecost Island,
    Penama Province ,Vanuatu as of 29 Oct. 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3716/UNOSAT_DamageAssessment_TC20231023VUT_PentacostIsland_TCLola23.xlsx
  format: null
  id: resource_47d9e234
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_DamageAssessment_TC20231023VUT_PentacostIsland_TCLola23.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_unosat_buildingsdamageassessment_20231101
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
  start: '2023-11-01'
temporal_resolution: null
title: Buildings Damage Assessment & Related Density over Pentecost Island, Penama
  Province ,Vanuatu as of 29 Oct. 2023
version: null
vulnerability: null
---
