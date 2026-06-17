---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-6-november-2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-6-november-2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-6-november-2
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-6-november-2
dataset_id: rdls_hel-phl_unosat_detectedwatersalbaycamari_20201106
description: 'UNOSAT code: TC20201101PHL This map illustrates satellite-detected surface
  waters in Albay and Camarines Sur provinces of Philippines as observed from a Sentinel-1
  image acquired on 6 November 2020 at 05:38 local time. Within the analyzed area
  of about 5,000 km2, a total of about 120 km2 of lands appear to be flooded. The
  water extent appears to have receded of about 120 km2 since 1 November 2020. Based
  on Worldpop population data and the detected surface waters, about 80,000 people
  are potentially exposed or living close to flooded areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT. Important Note: Flood analysis from radar images may underestimate
  the presence of standing waters in built-up areas and densely vegetated areas due
  to backscattering properties of the radar signal.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-6-november-2]'
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
    description: Estimated population potentially exposed to or living close to flooded
      areas, derived from WorldPop population data intersected with detected flood
      extent
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 C-band SAR imagery acquired on 6 November 2020 was analyzed
    by UNOSAT analysts using change detection methods, comparing the image against
    a pre-event reference to delineate satellite-detected surface water extent across
    Albay and Camarines Sur provinces following Typhoon Goni. The resulting flood
    footprint (~120 km2) was intersected with WorldPop population data to estimate
    the number of people potentially exposed, producing a preliminary emergency mapping
    product for humanitarian response.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/waters-in-albay-and-camarines-sur-provinces-bicol-region-of-philippines-as-of-6-november-2
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people potentially exposed to or living close
      to satellite-detected flooded areas (~80,000 people)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Satellite detected waters in Albay and Camarines Sur Provinces, Bicol
    Region of Philippines as of 6 November 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201101PHL/TC20201101PHL_gdb.zip
  format: Geodatabase
  id: resource_eb7fa45e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201101PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Albay and Camarines Sur Provinces, Bicol
    Region of Philippines as of 6 November 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20201101PHL/TC20201101PHL_SHP.zip
  format: null
  id: resource_c6cb3422
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20201101PHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_detectedwatersalbaycamari_20201106
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-06'
temporal_resolution: null
title: Satellite detected waters in Albay and Camarines Sur Provinces, Bicol Region
  of Philippines as of 6 November 2020
version: null
vulnerability: null
---
