---
attributions:
- entity:
    affiliation: null
    email: null
    name: Landsat 5-7 satellite data series
    url: https://data.humdata.org/dataset/mimu-geonode-ayeyarwady-river-bank-erosion
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SERVIR-Mekong programme
    url: https://data.humdata.org/dataset/mimu-geonode-ayeyarwady-river-bank-erosion
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-ayeyarwady-river-bank-erosion
creator:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-ayeyarwady-river-bank-erosion
dataset_id: rdls_hzd-mmr_mimu_ayeyarwadyriverbankerosio_1988
description: 'Outputs from seasonal river morphological monitoring system showing
  erosion and deposition areas along the Ayeyarwady River, Myanmar after the end of
  every monsoon season developed under the USAID funded SERVIR-Mekong programme. This
  dataset uses on Landsat 5-7 satellite data series covering 31-year time scale from
  1988 to 2019. You can find tiff files from 1988 to 2019 here : http://geonode.themimu.info/static/riverbankerosin.html
  https://myit-servir.adpc.net/ Original dataset title: Ayeyarwady river bank erosion
  1988-2019. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mimu-geonode-ayeyarwady-river-bank-erosion]'
details: "This product has been prepared for operational purposes only, to support\
  \ humanitarian and development activities in Myanmar. Copyright \xC2\xA92020 Myanmar\
  \ Information Management Unit. MIMU geospatial datasets cannot be used on online\
  \ platform unless with prior written agreement from MIMU. MIMU products are not\
  \ for sale and can be used free of charge with attribution. For more information\
  \ see http://themimu.info/mimu-terms-conditions."
exposure: []
hazard:
  event_sets_by_hazard_type:
    erosion:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: Er:T/ha
        process: soil_erosion
        trigger: null
        type: erosion
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Landsat 5-7 satellite imagery spanning 1988-2019 was processed through
    the SERVIR-Mekong seasonal river morphological monitoring system to detect and
    map erosion and deposition areas along the Ayeyarwady River. Multi-temporal analysis
    of optical satellite data identifies changes in river bank position and sediment
    dynamics at the end of each monsoon season, producing vector outputs (shapefile
    and GeoJSON) of erosion-affected zones.
  sources:
  - id: source_1
    license: null
    name: Landsat 5-7 satellite data series
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: SERVIR-Mekong programme
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mimu-geonode-ayeyarwady-river-bank-erosion
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?format_options=charset%3AUTF-8&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&typename=geonode:river_bank_erosion_2019
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Zipped Shapefile. Outputs from seasonal river morphological monitoring
    system showing erosion and deposition areas along the Ayeyarwady River, Myanmar
    after the end of every monsoon season developed under the USAID funded SERVIR-Mekong
    programme. This dataset uses on Landsat 5-7 satellite data series covering 31-year
    time scale from 1988 to 2019. You can find tiff files from 1988 to 2019 here :
    http://geonode.themimu.info/static/riverbankerosin.html'
  download_url: null
  format: null
  id: resource_a39f84e2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ayeyarwady river bank erosion shapefile
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&typeName=geonode:river_bank_erosion_2019
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'GeoJSON file. Outputs from seasonal river morphological monitoring
    system showing erosion and deposition areas along the Ayeyarwady River, Myanmar
    after the end of every monsoon season developed under the USAID funded SERVIR-Mekong
    programme. This dataset uses on Landsat 5-7 satellite data series covering 31-year
    time scale from 1988 to 2019. You can find tiff files from 1988 to 2019 here :
    http://geonode.themimu.info/static/riverbankerosin.html'
  download_url: null
  format: null
  id: resource_3f742e65
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ayeyarwady river bank erosion geojson
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mmr_mimu_ayeyarwadyriverbankerosio_1988
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-12-31'
  start: '1988-01-01'
temporal_resolution: null
title: Myanmar - Ayeyarwady river bank erosion
version: null
vulnerability: null
---
