---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-mocoa-colombia-situation-as-of-10-april-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-mocoa-colombia-situation-as-of-10-april-2017
dataset_id: rdls_hel-col_unosat_potentiallyaffectedzonesm_20170413
description: 'This map illustrates areas potentially affected by the mudflow, extracted
  from a Pleiades and GeoEye-1 satellite images acquired on the 10 April 2017 over
  Mocoa city and its outskirts, in Putumayo Department, Colombia. Inside some neighbourhoods
  of the city of Mocoa, flood waters and mudflow have receded compared with previous
  analysis performed by UNOSAT using an image from 4 April 2017. The situation as
  of 10 April 2017 reveals: 22 km of roads seem potentially affected and about 1,300
  buildings are within areas which are still experiencing floods and mud flow. It
  is likely that flood waters and mudflow could have been systematically under or
  overestimated along highly vegetated areas and within built-up urban areas. This
  analysis has not yet been validated in the field. Please send ground feedback to
  UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-mocoa-colombia-situation-as-of-10-april-2017]'
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
    description: Building stock within mudflow and flood-affected zones in Mocoa city
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
    description: Road network segments potentially affected by mudflow and flooding
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
  description: UNOSAT analysts performed multi-temporal satellite image analysis comparing
    Pleiades and GeoEye-1 imagery from 4 April and 10 April 2017 to map the spatial
    extent of mudflow and flood inundation in Mocoa following the 1 April 2017 disaster
    event. Affected areas were digitized and quantified to estimate building counts
    and road lengths within inundated zones.
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
- href: https://data.humdata.org/dataset/potentially-affected-zones-by-the-mudflow-in-mocoa-colombia-situation-as-of-10-april-2017
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Approximately 1,300 buildings within areas experiencing mudflow and
      flood inundation
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
    description: Approximately 22 km of roads potentially affected by mudflow and
      flooding
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
  description: Colombia - Potentially Affected Zones by the Mudflow in Mocoa (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL.gdb.zip
  format: Geodatabase
  id: resource_d7f29518
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Potentially Affected Zones by the Mudflow in Mocoa (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CO/LS20170403COL/LS20170403COL_SHP.zip
  format: null
  id: resource_11656331
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20170403COL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-col_unosat_potentiallyaffectedzonesm_20170413
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-13'
temporal_resolution: null
title: Colombia - Potentially Affected Zones by the Mudflow in Mocoa
version: null
vulnerability: null
---
