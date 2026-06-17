---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-landslide-inventory-of-freetown-sierra-leone-18-august-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-landslide-inventory-of-freetown-sierra-leone-18-august-2017
dataset_id: rdls_hl-sle_unosat_preliminarylandslideinven_20170818
description: 'This map shows landslides mapped from satellite imagery following the
  Regent event on 15 August 2017. The main landslide outline in Regent has been updated
  from the product released by UNITAR-UNOSAT (published 16 August, version 1.0) using
  the updated UNITAR-UNOSAT georectification of the satellite image on 17th August.
  The main Regent landslide event is 6 km long, including source area and run-out
  to the sea. It is interpreted as a debris slide in its upper reaches, transitioning
  to a debris flow and then a sediment-laden flood. The two smaller landslides are
  interpreted as debris flow events. The analysis has not yet been verified in the
  field.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-landslide-inventory-of-freetown-sierra-leone-18-august-2017]'
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
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired on
    15-17 August 2017 to map landslide extents and morphology following the Regent
    debris slide event. The main landslide outline was georectified and updated using
    satellite imagery from 17 August 2017, with interpretation of debris slide, debris
    flow, and sediment-laden flood transitions. Mapped features include source areas
    and run-out zones extending 6 km to the sea.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-landslide-inventory-of-freetown-sierra-leone-18-august-2017
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct impact of debris slide and flow event on natural environment
      and terrain
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
  description: Preliminary landslide inventory of Freetown, Sierra Leone 18 August
    2017 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SL/FL20170815SLE/FL20170815SLE_BGS_Data_gdb.zip
  format: Geodatabase
  id: resource_47561e96
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815SLE_BGS_Data_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary landslide inventory of Freetown, Sierra Leone 18 August
    2017 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SL/FL20170815SLE/FL20170815SLE_BGS_Data_shp.zip
  format: null
  id: resource_2af523df
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815SLE_BGS_Data_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-sle_unosat_preliminarylandslideinven_20170818
spatial:
  bbox: null
  centroid: null
  countries:
  - SLE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-18'
temporal_resolution: null
title: Preliminary landslide inventory of Freetown, Sierra Leone 18 August 2017
version: null
vulnerability: null
---
