---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-southeastern-freetown-sierra-leone
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-southeastern-freetown-sierra-leone
dataset_id: rdls_hel-sle_unosat_potentiallyaffectedzonesm_20170816
description: 'This map illustrates satellite-detected landslides and mudflow that
  affected Regent area south eastern Freetown using a GeoEye-1 acquired the 15 August
  2017 compared with a pre-crisis image acquired the 03 March 2017. UNOSAT extracted
  areas affected by the landslide and subsequent mudflow and could identify 349 damaged
  structure and 1.3 km of damaged roads within the analysed area. This analysis has
  not yet been validated in the field. Please send ground feedback to UNITAR /UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-southeastern-freetown-sierra-leone]'
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
    description: Building structures in the Regent area affected by landslide and
      mudflow
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
    description: Road network segments affected by mudflow damage
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
      quantity_kind: length
      unit: null
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
  description: UNOSAT analysts compared pre-crisis GeoEye-1 satellite imagery (03
    March 2017) with post-event imagery (15 August 2017) to detect landslide and mudflow
    extent in southeastern Freetown. Visual interpretation identified 349 damaged
    structures and 1.3 km of damaged roads within the affected zone. The analysis
    was conducted through manual satellite image analysis without field validation.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-southeastern-freetown-sierra-leone
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and mudflow event (349 damaged
      structures identified)
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
    description: Direct road infrastructure damage from mudflow (1.3 km of damaged
      roads)
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
  description: Potentially Affected Zones by the Mudflow in southeastern Freetown,
    Sierra Leone (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SL/FL20170815SLE/FL20170815SLE_gdb.zip
  format: Geodatabase
  id: resource_266e2325
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815SLE_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Potentially Affected Zones by the Mudflow in southeastern Freetown,
    Sierra Leone (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SL/FL20170815SLE/FL20170815SLE_shp.zip
  format: null
  id: resource_41520396
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815SLE_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sle_unosat_potentiallyaffectedzonesm_20170816
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
  start: '2017-08-16'
temporal_resolution: null
title: Potentially Affected Zones by the Mudflow in southeastern Freetown, Sierra
  Leone
version: null
vulnerability: null
---
