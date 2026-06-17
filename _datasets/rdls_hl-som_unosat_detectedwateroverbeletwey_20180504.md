---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-belet-weyne-district-2789
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-belet-weyne-district-2789
dataset_id: rdls_hl-som_unosat_detectedwateroverbeletwey_20180504
description: 'This map illustrates satellite-detected flood water extent within the
  town of Belet Weyne in Belet Weyne District,Hiiran Region, Somalia. The analysis
  was conducted analyzing GeoEye-1 image acquired on the 30 April 2018. As observed
  from the satellite image, the town of Belet Weyne is completely affected by the
  floods. More than 50% of the extension of the town is totally inundated, being the
  districts of Bulahabley, Bundaweyn, Dhagahjebis, Hilac, Hindab and Lamagalay Regional
  Military Based completely submerged in water. The areas of partially flooded districts
  present affected roads and buildings. Districts located in the north of the town
  are partially or completely obscured by the clouds but they might be totally flooded
  as well, due to the observations in the surrounding areas of the district. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-belet-weyne-district-2789]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts analyzed GeoEye-1 satellite imagery acquired on 30
    April 2018 over Belet Weyne town, comparing multi-temporal images to detect flood
    water extent and identify inundated districts. The resulting vector dataset delineates
    areas of complete and partial inundation with confidence levels and field validation
    records.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-over-belet-weyne-town-belet-weyne-district-2789
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding in Belet Weyne, with
      >50% of town inundated
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
  description: Somalia - Satellite detected water over Belet Weyne Town, Belet Weyne
    District (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SO/FL20180501SOM/FL20180501SOM_SHP.zip
  format: null
  id: resource_c5c872d7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180501SOM_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_unosat_detectedwateroverbeletwey_20180504
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-04'
temporal_resolution: null
title: Somalia - Satellite detected water over Belet Weyne Town, Belet Weyne District
version: null
vulnerability: null
---
