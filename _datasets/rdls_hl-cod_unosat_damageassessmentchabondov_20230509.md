---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-chabondo-village-kalehe-territory-sud-kivu-province-dr-of-the-congo-a
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-chabondo-village-kalehe-territory-sud-kivu-province-dr-of-the-congo-a
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-chabondo-village-kalehe-territory-sud-kivu-province-dr-of-the-congo-a
dataset_id: rdls_hl-cod_unosat_damageassessmentchabondov_20230509
description: 'UNOSAT code FL20230508COD, GDACS Id: 1101981 This map illustrates the
  potentially damaged structures/buildings affected by landslides in Chabondo village,
  Kalehe Territory, Sud-Kivu Province, DR. of the Congo as detected from a Pleiades
  image acquired on the 09th May 2023. Within the extent of this map, at least 544
  structures appear to be affected or potentially affected by landslides. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-chabondo-village-kalehe-territory-sud-kivu-province-dr-of-the-congo-a]'
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 09
    May 2023 and compared it with reference imagery to detect structural damage caused
    by landslides in Chabondo village. Visual interpretation and change detection
    methods identified 544 potentially affected buildings. The preliminary assessment
    was delivered as vector geodatabase and shapefile formats with building footprints
    and damage attributes.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-chabondo-village-kalehe-territory-sud-kivu-province-dr-of-the-congo-a
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslides affecting 544 structures in
      Chabondo village
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: Damage assessment in Chabondo village, Kalehe Territory, Sud-Kivu Province,
    DR. of the Congo as of 09 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3580/FL20230508COD_gdb.zip
  format: Geodatabase
  id: resource_188586bb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230508COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in Chabondo village, Kalehe Territory, Sud-Kivu Province,
    DR. of the Congo as of 09 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3580/FL20230508COD_SHP.zip
  format: null
  id: resource_2c2239be
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230508COD_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cod_unosat_damageassessmentchabondov_20230509
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-09'
temporal_resolution: null
title: Damage assessment in Chabondo village, Kalehe Territory, Sud-Kivu Province,
  DR. of the Congo as of 09 May 2023
version: null
vulnerability: null
---
