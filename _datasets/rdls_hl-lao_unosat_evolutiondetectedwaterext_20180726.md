---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-
dataset_id: rdls_hl-lao_unosat_evolutiondetectedwaterext_20180726
description: 'This map illustrates the evolution of satellite-detected surface waters
  in Sanamxay district, Attapeu province, as observed from the Radarsat-2 radar image
  acquired on 24 July 2018 and compared with a Radsarsat-2 image acquired on 10 July
  2018. As of 10 July 2018, flooded areas and saturated soils were already visible,
  due to the heavy rains that happened previously to the collapse of the dam. As well,
  the reservoir controlled by the dam was full of water. As of 24 July 2018, an additional
  surface of 5,826 ha of inundated areas were detected, representing an increase of
  the surface waters of 66%, due to the collapse of the dam. At this date, the reservoir
  that was controlled by the dam has decreased in its size. Several villages and surrounding
  agricultural fields seems to be inundated. The villages of Ban Hinlat, Ban Thaseangchan,
  Ban Mai and Ban Samong-tai seems to be the most affected ones. It is likely that
  flood waters have been systematically underestimated along highly vegetated areas,
  along the main riverbanks and within built-up urban areas because of the special
  characteristics of the used satellite data. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-]'
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared Radarsat-2 radar imagery acquired on 10 July
    2018 and 24 July 2018 to detect changes in surface water extent following the
    dam collapse in Attapeu Province. The analysis identified an additional 5,826
    hectares of inundated areas through visual interpretation and change detection
    between the two satellite images, with confidence levels and field validation
    recorded for each mapped water polygon.
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
- href: https://data.humdata.org/dataset/evolution-satellite-detected-water-extent-over-sanamxay-district-attapeu-province-lao-people-
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct inundation of 5,826 hectares of land surface detected by satellite
      radar imagery
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
  description: Evolution satellite detected water extent over Sanamxay District, Attapeu
    Province, Lao People Democratic Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20180723LAO/FL20180723LAO_shp.zip
  format: null
  id: resource_7b1f67d5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180723LAO_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lao_unosat_evolutiondetectedwaterext_20180726
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-26'
temporal_resolution: null
title: Evolution satellite detected water extent over Sanamxay District, Attapeu Province,
  Lao People Democratic Republic
version: null
vulnerability: null
---
