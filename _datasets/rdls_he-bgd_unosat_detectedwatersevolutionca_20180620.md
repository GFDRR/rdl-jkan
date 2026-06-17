---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNOSAT
    url: https://data.humdata.org/dataset/satellite-detected-waters-evolution-by-camp-extent-in-cox-s-bazar-district-chittagong-division-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-evolution-by-camp-extent-in-cox-s-bazar-district-chittagong-division-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-evolution-by-camp-extent-in-cox-s-bazar-district-chittagong-division-
dataset_id: rdls_he-bgd_unosat_detectedwatersevolutionca_20180620
description: 'This map illustrates the evolution of satellite detected waters and
  the related wet conditions in the Cox''s Bazar Myanmar nationals refugee camps located
  in Ukhia Upazilla, as deduced from the analysis of two Radarsat-2 Spotlight images
  with 0.5m resolution acquired on 16 June 2018 & 23 May 2018. The evolution of surface
  waters was classified into three classes of change: low, moderate and high. This
  analysis shows that some camps experienced a lower increase of wet conditions/surface
  waters, as camp 1W and camp 2E. Whereas some have moderately changed, as camp 2W,
  camp 6 and camp 14, others have greatly changed, as camp 17, camp 8W and camp 20
  and its extension. It is likely that flood waters have been systematically underestimated
  along highly vegetated areas along main river banks and within built-up urban areas
  because of the special characteristics of the satellite data used. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-evolution-by-camp-extent-in-cox-s-bazar-district-chittagong-division-]'
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
    description: Myanmar nationals refugee camp populations in Ukhia Upazilla, Cox's
      Bazar, spatially delineated by camp extent polygons
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Two Radarsat-2 Spotlight SAR images (0.5m resolution) acquired on 23
    May 2018 and 16 June 2018 were analyzed by UNOSAT to detect changes in surface
    water extent within Myanmar nationals refugee camps in Ukhia Upazilla, Cox's Bazar.
    Change in mean backscatter values between the two acquisition dates was computed
    per camp polygon and classified into three levels of wet condition change (low,
    moderate, high). The resulting dataset provides a spatially explicit record of
    flood/inundation evolution overlaid on camp boundaries to support humanitarian
    response planning.
  sources:
  - id: source_1
    license: null
    name: UNOSAT
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-evolution-by-camp-extent-in-cox-s-bazar-district-chittagong-division-
  rel: source
loss: null
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
  description: Satellite Detected Waters Evolution by Camp Extent in Cox's Bazar District,
    Chittagong Division, Bangladesh (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20180518BGD/FL20180518BGD_SHP.zip
  format: null
  id: resource_6fc9affc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180518BGD_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-bgd_unosat_detectedwatersevolutionca_20180620
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-06-20'
temporal_resolution: null
title: Satellite Detected Waters Evolution by Camp Extent in Cox's Bazar District,
  Chittagong Division, Bangladesh
version: null
vulnerability: null
---
