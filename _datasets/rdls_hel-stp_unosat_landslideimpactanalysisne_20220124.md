---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-neves-town-lemba-district-sao-tome-province-sao-tome-and-prin
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-neves-town-lemba-district-sao-tome-province-sao-tome-and-prin
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-neves-town-lemba-district-sao-tome-province-sao-tome-and-prin
dataset_id: rdls_hel-stp_unosat_landslideimpactanalysisne_20220124
description: "UNOSAT code: FL20220119STP This map illustrates satellite-detected landslides/mudflow\
  \ in Neves town, Lemb\xE1 district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and\
  \ Pr\xEDncipe as observed in Pleiades satellite imagery acquired on 23 January 2022\
  \ at 10:12 local time. Within this analyzed area, about 10 structures appear to\
  \ be affected, and 63 structures are potentially affected. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to United Nations Satellite Centre (UNOSAT). [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/landslide-impact-analysis-in-neves-town-lemba-district-sao-tome-province-sao-tome-and-prin]"
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
    description: Building structures in Neves town classified by damage status from
      landslide/mudflow event
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
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 23
    January 2022 and performed visual interpretation and change detection to identify
    satellite-detected landslides and mudflow features in Neves town. Building structures
    were then assessed for damage status (affected vs. potentially affected) based
    on spatial proximity to detected hazard features. This preliminary analysis has
    not been validated in the field.
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-neves-town-lemba-district-sao-tome-province-sao-tome-and-prin
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and mudflow event with 10 structures
      affected and 63 potentially affected
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
  description: "Sao Tome and Principe - Landslide impact analysis in Neves town, Lemb\xE1\
    \ district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and Pr\xEDncipe as of 23 Jan\
    \ 2022 (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/ST/FL20220119STP/FL20220119STP_gdb.zip
  format: Geodatabase
  id: resource_db60a40c
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
  description: "Sao Tome and Principe - Landslide impact analysis in Neves town, Lemb\xE1\
    \ district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and Pr\xEDncipe as of 23 Jan\
    \ 2022 (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/ST/FL20220119STP/FL20220119STP_SHP.zip
  format: null
  id: resource_0adf217b
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
slug: rdls_hel-stp_unosat_landslideimpactanalysisne_20220124
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
  start: '2022-01-24'
temporal_resolution: null
title: "Sao Tome and Principe - Landslide impact analysis in Neves town, Lemb\xE1\
  \ district, S\xE3o Tom\xE9 province, S\xE3o Tom\xE9 and Pr\xEDncipe as of 23 Jan\
  \ 2022"
version: null
vulnerability: null
---
