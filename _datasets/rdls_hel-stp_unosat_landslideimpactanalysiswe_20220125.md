---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-western-part-of-lemba-district-sao-tome-province-sao-tome-and
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-western-part-of-lemba-district-sao-tome-province-sao-tome-and
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-western-part-of-lemba-district-sao-tome-province-sao-tome-and
dataset_id: rdls_hel-stp_unosat_landslideimpactanalysiswe_20220125
description: "UNOSAT code: FL20220119STP This map illustrates satellite-detected landslides/mudflow\
  \ in western part of Lemb\xE1 district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9\
  \ and Pr\xEDncipe as observed in Pleiades satellite imagery acquired on 23 January\
  \ 2022 at 10:12 local time. Within the analyzed area, about 5 structures appear\
  \ to be affected, and 23 structures are potentially affected. 2 road obstacles,\
  \ 2 affected bridges, and a potentially affected bridge were also identified. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-western-part-of-lemba-district-sao-tome-province-sao-tome-and]"
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
    description: Building structures in the affected area, classified by damage status
      (affected vs. potentially affected)
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
    description: Road and bridge infrastructure in the study area, including obstacles
      and damage status
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
  description: Pleiades satellite imagery acquired on 23 January 2022 was analyzed
    by UNOSAT analysts through visual interpretation and comparison with reference
    imagery to detect landslide and mudflow features. Affected and potentially affected
    structures and infrastructure were identified and mapped in vector format (geodatabase
    and shapefile). This preliminary post-event damage assessment has not been field-validated.
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-western-part-of-lemba-district-sao-tome-province-sao-tome-and
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from landslide/mudflow events: 5 structures
      affected, 23 potentially affected'
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
    description: 'Direct infrastructure damage from landslide/mudflow events: 2 road
      obstacles, 2 affected bridges, 1 potentially affected bridge'
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
  description: "Sao Tome and Principe - Landslide impact analysis in western part\
    \ of Lemb\xE1 district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and Pr\xEDncipe\
    \ as of 23 Jan 2022 (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/ST/FL20220119STP/FL20220119STP_gdb.zip
  format: Geodatabase
  id: resource_04956c9d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220119STP_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Sao Tome and Principe - Landslide impact analysis in western part\
    \ of Lemb\xE1 district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and Pr\xEDncipe\
    \ as of 23 Jan 2022 (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/ST/FL20220119STP/FL20220119STP_SHP.zip
  format: null
  id: resource_48d571ae
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220119STP_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-stp_unosat_landslideimpactanalysiswe_20220125
spatial:
  bbox: null
  centroid: null
  countries:
  - STP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-25'
temporal_resolution: null
title: "Sao Tome and Principe - Landslide impact analysis in western part of Lemb\xE1\
  \ district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and Pr\xEDncipe as of 23 Jan\
  \ 2022"
version: null
vulnerability: null
---
