---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-bura-ub-county-tana-river-county-kenya-2798
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-bura-ub-county-tana-river-county-kenya-2798
dataset_id: rdls_hel-ken_unosat_detectedwateralongtanariv_20180511
description: 'This map illustrates satellite-detected flood water extent along Tana
  River, Bura Sub County, Kenya. The analysis was conducted analyzing Sentinel-1 image
  acquired on the 4 May 2018. The analysis extent is focused on the river bed of Tana
  and the surrounding land between the primary road and the limit of the Tana River
  boundary, specifically were the population is concentrated. Within the analysis
  extent, more than 9,100 ha of land appear to be inundated and more than 9,800 people
  are living inside this flood water extent. It is likely that flood waters have been
  systematically underestimated along highly vegetated areas along main river banks
  and within built-up urban areas because of the special characteristics of the satellite
  data used. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-bura-ub-county-tana-river-county-kenya-2798]'
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
    description: Population living within satellite-detected flood water extent along
      Tana River
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-1 SAR imagery acquired on 4 May 2018 was analyzed by UNOSAT
    using multi-temporal comparison and change detection methods to delineate flood
    water extent. The analysis focused on the Tana River bed and surrounding populated
    areas in Bura Sub County, producing a polygon vector dataset of inundated areas
    with calculated extent metrics (9,100 ha) and affected population estimates (9,800
    people).
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
- href: https://data.humdata.org/dataset/satellite-detected-water-along-tana-river-bura-ub-county-tana-river-county-kenya-2798
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by fluvial flooding detected via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
  description: Satellite detected water along Tana River, Bura ub county, Tana River
    county, Kenya (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/KE/FL20180508KEN/FL20180508KEN_shp.zip
  format: null
  id: resource_48651368
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180508KEN_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_detectedwateralongtanariv_20180511
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-11'
temporal_resolution: null
title: Satellite detected water along Tana River, Bura ub county, Tana River county,
  Kenya
version: null
vulnerability: null
---
