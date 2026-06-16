---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/mudslide-impact-in-jalal-abad-regions-kyrgyzstan-as-of-30-july-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudslide-impact-in-jalal-abad-regions-kyrgyzstan-as-of-30-july-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudslide-impact-in-jalal-abad-regions-kyrgyzstan-as-of-30-july-2024
dataset_id: rdls_hel-kgz_unosat_mudslideimpactjalalabadre_20240805
description: "UNOSAT code: FL20240725KGZ This map illustrates satellite-detected mudslides\
  \ in Bazar-Korgon District, Jalal-Abad Region, Kyrgyzstan, as observed from a WorldView-3\
  \ satellite image acquired on July 27, 2024, and Global satellites acquired on July\
  \ 27, 28, and 30, 2024. Within the analyzed area of approximately 280 km\xB2, about\
  \ 1 km\xB2 of mudslide extent was observed. Additionally, within this area, 23 buildings\
  \ (less than 1% of the total structures) were identified as affected by the mudslide.\
  \ Approximately 5 bridges were observed destroyed as of May 20, 2024. This is a\
  \ preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/mudslide-impact-in-jalal-abad-regions-kyrgyzstan-as-of-30-july-2024]"
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
    description: Building stock in the analyzed area, with 23 structures identified
      as affected by mudslide
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
- asset_type:
    description: Bridge infrastructure in the study area, with 5 bridges observed
      destroyed
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: LSI:-
        process: landslide_mudflow
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed multi-temporal satellite imagery (WorldView-3\
    \ and Global satellites from July 27-30, 2024) through visual comparison to detect\
    \ mudslide occurrence and extent in Bazar-Korgon District. Affected buildings\
    \ and destroyed bridges were identified through direct visual interpretation of\
    \ satellite imagery within the 280 km\xB2 study area."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mudslide-impact-in-jalal-abad-regions-kyrgyzstan-as-of-30-july-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from mudslide impact, 23 structures affected
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure loss from mudslide, 5 bridges destroyed
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Mudslide impact in Jalal-Abad Regions, Kyrgyzstan as of 30 July 2024
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3907/FL20240725KGZ_GDB.zip
  format: Geodatabase
  id: resource_3a27d34b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240725KGZ_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mudslide impact in Jalal-Abad Regions, Kyrgyzstan as of 30 July 2024
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3907/FL20240725KGZ_SHP.zip
  format: null
  id: resource_edc4437b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240725KGZ_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-kgz_unosat_mudslideimpactjalalabadre_20240805
spatial:
  bbox: null
  centroid: null
  countries:
  - KGZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-08-05'
temporal_resolution: null
title: Mudslide impact in Jalal-Abad Regions, Kyrgyzstan as of 30 July 2024
version: null
vulnerability: null
---
