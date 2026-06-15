---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/287
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/287
dataset_id: rdls_hzd-png_pacificdata_pgeqhazardmap102500mrp
description: 'An earthquake hazard map provides, at any location, the value of a ground
  motion intensity measure (for example, horizontal peak ground acceleration, PGA)
  that is expected to be exceeded at least once in 2500 year mean return period. The
  earthquake hazard maps are developed by determining the simulated ground motion
  intensities at every gridded location for 10,000 realizations of next-year activity
  of earthquake events. At each grid location, the intensities are ranked and the
  ground motion intensity of the mean return period of interest is recorded. Spectral
  = 1 second spectral acceleration. The size of the finest grid is 9 arc seconds and
  was resampled to coarser resolutions (up to approximately 7 arc minutes) for some
  locations. Compiled by AIR Worldwide. [Source: This metadata record was automatically
  extracted from the GeoNode portal pacificdata]'
details: Hazard Earthquake Probabilistic
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: null
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_earthquake
          intensity_measure: PGA:g
          process: ground_motion
          trigger: null
          type: earthquake
        id: event_2500yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.0004
            probability: null
            return_period: 2500
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
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
- href: https://geonode.pacificdata.org/catalogue/#/dataset/287
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
  description: Papua New Guinea Earthquake Hazard Map, 1.0s Spectral Acceleration,
    2500-year Return Period
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__png_10_2500t&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://geonode.pacificdata.org/datasets/geonode:png_10_2500t
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Papua New Guinea Earthquake Hazard Map, 1.0s Spectral Acceleration,
    2500-year Return Period (OGC WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:png_10_2500t&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:png_10_2500t
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Papua New Guinea Earthquake Hazard Map, 1.0s Spectral Acceleration,
    2500-year Return Period (OGC WCS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__png_10_2500t
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
slug: rdls_hzd-png_pacificdata_pgeqhazardmap102500mrp
spatial:
  bbox:
  - 140.840535
  - -11.65042
  - 159.480535
  - -0.76042
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2020
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Papua New Guinea Earthquake Hazard Map, 1.0s Spectral Acceleration, 2500-year
  Return Period
version: null
vulnerability: null
---
