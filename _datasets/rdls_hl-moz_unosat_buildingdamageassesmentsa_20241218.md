---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/building-damage-assesment-in-sambene-nanguasse-muinde-villages-mecufi-posto-mecufi-distric
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assesment-in-sambene-nanguasse-muinde-villages-mecufi-posto-mecufi-distric
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assesment-in-sambene-nanguasse-muinde-villages-mecufi-posto-mecufi-distric
dataset_id: rdls_hl-moz_unosat_buildingdamageassesmentsa_20241218
description: 'UNOSAT code: TC20241212MOZ, GDACS ID: 1001131 This map illustrates affected
  structures in Mecufi Posto, Mecufi District, Cabo Delgado Province as observed from
  a Pleiades satellite image acquired on 17 December 2024 at 07:51 Local Time. Within
  the analysed area, UNOSAT identified 2,433 destroyed structures and 1,684 damaged
  structures amongst a total of 4,118 structures observed. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage-assesment-in-sambene-nanguasse-muinde-villages-mecufi-posto-mecufi-distric]'
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 17
    December 2024 over Mecufi Posto, Mecufi District, Cabo Delgado Province, Mozambique,
    and performed visual interpretation and change detection to classify structures
    as destroyed, damaged, or undamaged. The resulting damage assessment dataset contains
    4,118 mapped structures with damage classification and confidence levels, representing
    direct impacts from tropical cyclone TC20241212MOZ.
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
- href: https://data.humdata.org/dataset/building-damage-assesment-in-sambene-nanguasse-muinde-villages-mecufi-posto-mecufi-distric
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from tropical cyclone: 2,433 destroyed and
      1,684 damaged structures identified via satellite analysis'
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
  description: Mozambique - Building Damage Assesment in Sambene, Nanguasse & Muinde
    villages, Mecufi Posto, Mecufi District as of 17 December 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4056/TC20241212MOZ_gdb.zip
  format: Geodatabase
  id: resource_dcd14fc1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241212MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique - Building Damage Assesment in Sambene, Nanguasse & Muinde
    villages, Mecufi Posto, Mecufi District as of 17 December 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4056/TC20241212MOZ_SHP.zip
  format: null
  id: resource_5124d6a4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241212MOZ_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-moz_unosat_buildingdamageassesmentsa_20241218
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-12-18'
temporal_resolution: null
title: Mozambique - Building Damage Assesment in Sambene, Nanguasse & Muinde villages,
  Mecufi Posto, Mecufi District as of 17 December 2024
version: null
vulnerability: null
---
