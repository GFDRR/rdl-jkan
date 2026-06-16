---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
creator:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
dataset_id: rdls_hzd-uga_icpac_floodinundation100yearret
description: 'This dataset is the output from the Global Flood Model intercomparison
  project undertaken on behalf of the Global Flood Partnership. The methodology is
  described in Trigg et al., 2016, ''The credibility challenge for global fluvial
  flood risk analysis,'' published in the Environmental Research Letters Journal.
  Each file is a geospatial, WGS84, 1/1200 ( 0.000833) decimal degrees resolution
  (~90m) GeoTIFF raster with a classified integer value representing how many out
  of the 6 models agree that a cell is wet (note 0 - dry/no data) [Source: This metadata
  record was automatically extracted from the GeoNode portal icpac]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: IGAD DRM Team
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/Uganda_flood_inundation:geonode:Uganda_flood_inundation
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net
purpose: 'component- Exposure Source : University Of Leeds Format : TIFF purpose-
  The flood inundation shows water that is excess to a river channel capacity inundates
  the sorrounding floodplain topography'
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:Uganda_flood_inundation
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Uganda Flood Inundation (100 year return period) (OGC WMS: geonode
    Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:Uganda_flood_inundation&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:Uganda_flood_inundation
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Uganda Flood Inundation (100 year return period) (OGC WCS: geonode
    Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:Uganda_flood_inundation
  format: null
  id: resource_1
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
slug: rdls_hzd-uga_icpac_floodinundation100yearret
spatial:
  bbox:
  - 29.572495188812187
  - -1.479165295101152
  - 34.99999415171853
  - 4.234166946521127
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Uganda Flood Inundation (100 year return period)
version: null
vulnerability: null
---
