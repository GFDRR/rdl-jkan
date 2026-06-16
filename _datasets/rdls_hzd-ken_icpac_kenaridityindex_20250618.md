---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ken-aridity-index
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ken-aridity-index
dataset_id: rdls_hzd-ken_icpac_kenaridityindex_20250618
description: 'Aridity index (AI) is an effective estimator of drought status, and
  spatiotemporally continuous long-term AI dataset is critical for drought assessment
  and applications.This dataset offers valuable support for research on dryland ecosystems,
  agriculture, and climate change, offering critical insights to address global environmental
  and sustainability challenges. Resolution ;0.05 &times; 0.05 in the resolution (
  referenced year 2022). [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-ken-aridity-index]'
details: Time period is set to publication date rather than the date the data covers
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: "Aridity index (AI) values were calculated from long-term climate data\
    \ and spatially interpolated to produce a continuous raster dataset at 0.05\xC2\
    \xB0 resolution referenced to 2022, providing a spatiotemporal characterization\
    \ of drought hazard for dryland ecosystem and agricultural applications."
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-ken-aridity-index
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__Normalized_KEN_aridity_avg_Copy&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. Aridity index (AI) is an effective estimator of drought
    status, and spatiotemporally continuous long-term AI dataset is critical for drought
    assessment and applications.This dataset offers valuable support for research
    on dryland ecosystems, agriculture, and climate change, offering critical insights
    to address global environmental and sustainability challenges. Resolution ;0.05
    &times; 0.05 in the resolution ( referenced year 2022)
  download_url: null
  format: null
  id: resource_3beeacc1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: KEN_aridity Index GeoTIFF
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ken_icpac_kenaridityindex_20250618
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
  start: '2025-06-18'
temporal_resolution: null
title: Kenya - KEN_aridity Index
version: null
vulnerability: null
---
