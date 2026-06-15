---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/292
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/292
dataset_id: rdls_hzd-tls_pacificdata_tltchazardmapwind100mrp
description: 'A tropical cyclone wind hazard map provides, at any location, the value
  of a wind intensity measure (for example, maximum 1 minute sustained wind speed
  for tropical cyclones) that is expected to be exceeded at least once in 100 year
  time period. The hazard maps are developed by determining the simulated intensities
  at every gridded location for 10,000 realizations of next-year activity of tropical
  cyclone events. At each grid location, the intensities are ranked and the wind intensity
  of the mean return period of interest is recorded. The size of the grid is 90 arc
  seconds. Compiled by AIR Worldwide. [Source: This metadata record was automatically
  extracted from the GeoNode portal pacificdata]'
details: Hazard Cyclone Probabilistic
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_strong_wind
          intensity_measure: sws_10m:m/s
          process: tropical_cyclone
          trigger: null
          type: strong_wind
        id: event_100yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability: null
            return_period: 100
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/292
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Timor-Leste Tropical Cyclone Wind Hazard Map, 100-year Return Period
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__tim_w100_tr&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://geonode.pacificdata.org/datasets/geonode:tim_w100_tr
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Timor-Leste Tropical Cyclone Wind Hazard Map, 100-year Return Period
    (OGC WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:tim_w100_tr&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:tim_w100_tr
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Timor-Leste Tropical Cyclone Wind Hazard Map, 100-year Return Period
    (OGC WCS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__tim_w100_tr
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tls_pacificdata_tltchazardmapwind100mrp
spatial:
  bbox:
  - 124.044647216797
  - -9.504650115967001
  - 127.342147216797
  - -8.126150115967
  centroid: null
  countries:
  - TLS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2020
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Timor-Leste Tropical Cyclone Wind Hazard Map, 100-year Return Period
version: null
vulnerability: null
---
